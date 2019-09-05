from xml.dom import minidom
xmldoc = minidom.parse("hiwiki-20190601-pages-articles-multistream.xml")
mediawiki = xmldoc.getElementsByTagName("mediawiki")[0]
siteinfo = mediawiki.getElementsByTagName("siteinfo")[0]
sitename = siteinfo.getElementsByTagName("sitename")[0]
print(sitename)
