import lxml.html


def tyusyutu(html):
    root = lxml.html.fromstring(html)
    centers = root.xpath(
        '//tr[@onmouseout="TRMouseOut(this)" and @onmouseover="TRMouseOver(this)"]/td[@align="center"]')
    rights = root.xpath(
        '//tr[@onmouseout="TRMouseOut(this)" and @onmouseover="TRMouseOver(this)"]/td[@align="right"]')
    lefts = root.xpath(
        '//tr[@onmouseout="TRMouseOut(this)" and @onmouseover="TRMouseOver(this)"]/td[@align="left"]')
    ahrefs = root.xpath(
        '//tr[@onmouseout="TRMouseOut(this)" and @onmouseover="TRMouseOver(this)"]/td[@align="left"]/a')
    i = 0
    j = 0
    k = 0
    for right in rights:
        # print(anchor.text)
        yield(right.text, centers[i].text, centers[i+1].text, centers[i+2].text, centers[i+3].text, ahrefs[j].text, ahrefs[j].get("href"), lefts[k+1].text)
        i += 4
        j += 1
        k += 2
