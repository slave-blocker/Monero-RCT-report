// Conserva as remissões internas do capítulo e aponta as restantes para o livro.
var doc = new PDFDocument(scriptArgs[0]);
var output = scriptArgs[1], first = Number(scriptArgs[2]) - 1, last = Number(scriptArgs[3]) - 1;
var chapterName = scriptArgs[4], bookPath = scriptArgs[5];
var catalog = doc.getTrailer().Root;
var pageIds = {};
for (var i = first; i <= last; ++i) {
    pageIds[doc.findPage(i).asIndirect()] = i;
}

var localNames = {}, kept = doc.newArray(), printed = 0;
function collect(node) {
    if (node.Kids) {
        node.Kids.forEach(function (child) { collect(child); });
        return;
    }
    for (var i = 0; i < node.Names.length; i += 2) {
        var key = node.Names[i], value = node.Names[i + 1];
        var dest = value.isArray() ? value : value.D;
        var page = pageIds[dest[0].asIndirect()];
        if (page === undefined) continue;
        kept.push(key);
        kept.push(value);
        var name = key.asString();
        localNames[name] = true;
        if (page === first && /^page\.[0-9]+$/.test(name)) printed = Number(name.slice(5));
    }
}
collect(catalog.Names.Dests);

function chapterOutline(node) {
    for (; node; node = node.Next) {
        if (node.A && node.A.D && node.A.D.asString() === chapterName) return node;
        var child = chapterOutline(node.First);
        if (child) return child;
    }
}
var outlines = catalog.Outlines;
var chapter = chapterOutline(outlines.First);
if (!chapter || !printed || !localNames[chapterName]) throw Error("Início de capítulo inválido.");
outlines.put("First", chapter);
outlines.put("Last", chapter);
outlines.put("Count", 1 + Math.max(0, Number(chapter.Count || 0)));
chapter.put("Parent", outlines);
chapter.delete("Next");
chapter.delete("Prev");

for (var i = first; i <= last; ++i) {
    var annotations = doc.findPage(i).Annots;
    if (!annotations) continue;
    annotations.forEach(function (annotation) {
        var action = annotation.A;
        if (!action || action.S.asName() !== "GoTo") return;
        var target = action.D.asString();
        if (!localNames[target]) {
            if (!doc.lookupDest(action.D)) throw Error("Destino desconhecido: " + target);
            action.put("S", doc.newName("GoToR"));
            action.put("F", doc.newString(bookPath));
        }
    });
}

catalog.Names.put("Dests", {Names: kept});
catalog.put("PageLabels", {Nums: [0, {S: doc.newName("D"), St: printed}]});
catalog.delete("OpenAction");
for (var i = doc.countPages() - 1; i > last; --i) doc.deletePage(i);
for (var i = first - 1; i >= 0; --i) doc.deletePage(i);
doc.save(output, "garbage=compact,compress");
