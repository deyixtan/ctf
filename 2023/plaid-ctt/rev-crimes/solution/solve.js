const getGroupByIdx = (groupIdx) => {
    return document.querySelector(`body > div:nth-child(1) > div:nth-child(${Number(9 + groupIdx)}) > div:nth-child(7)`);
}

const getGroupTopOpenings = (groupElem) => {
    // opening divs idx 79 - 84
    const topResults = [];
    for (let i = 0; i < 4; i++) {
        currElem = groupElem.querySelector(`div > div:nth-child(${i + 79}) > div`).style.background;
        svgEncoded = currElem.substring(currElem.indexOf("base64,") + 7, currElem.lastIndexOf("\""));
        svgDecoded = atob(svgEncoded);
        topOpening = svgDecoded.substring(svgDecoded.indexOf("M2 ") + 3);
        topOpening = topOpening.substring(0, topOpening.indexOf("V")); 
        topResults.push(Number(topOpening));
    }
    return topResults;
}

const verifyGroupStatus = (groupElem, topOpenings) => {
    for (let i = 0; i < 4; i++) {
        currElem = groupElem.querySelector(`div > div:nth-child(${i + 79}) > div`);
        currElemStyle = getComputedStyle(currElem);
        const currElemTop = Number(currElemStyle.top.split("px")[0]);
        if (currElemTop + topOpenings[i] - 2 != 60)
            return false;
    }
    return true;
}

const clickBtn = (groupElem, btnIdx) => {
    groupElem.querySelector(`div > details:nth-child(${btnIdx})`).open = !(groupElem.querySelector(`div > details:nth-child(${btnIdx})`).open || false);
}

const bruteforceRight = (groupElem, topOpenings) => {
    for (let i = 78; i >= 53; i--) {
        if (verifyGroupStatus(groupElem, topOpenings))
            return true;
        clickBtn(groupElem, i);
        if (verifyGroupStatus(groupElem, topOpenings))
            return true;
    }
    // Restore state
    for (let i = 53; i <= 78; i++) {
        clickBtn(groupElem, i);
    }
    return false;
}

const bruteforceMid = (groupElem, topOpenings) => {
    if (bruteforceRight(groupElem, topOpenings))
        return true;
    for (let i = 52; i >= 27; i--) {
        clickBtn(groupElem, i);
        if (bruteforceRight(groupElem, topOpenings))
            return true;
    }
    // Restore state
    for (let i = 27; i <= 52; i++) {
        clickBtn(groupElem, i);
    }
    return false;
}

const bruteforceLeft = (groupElem, topOpenings) => {
    if (bruteforceMid(groupElem, topOpenings))
        return true;
    for (let i = 26; i >= 1; i--) {
        clickBtn(groupElem, i);
        if (bruteforceMid(groupElem, topOpenings))
            return true;
    }
    // Restore state
    for (let i = 1; i <= 26; i++) {
        clickBtn(groupElem, i);
    }
    return false;
}

const bruteforceGroup = (groupIdx) => {
    // left btn: 26->1
    // mid btn: 52->27
    // right btn: 78->53
    const groupElem = getGroupByIdx(groupIdx);
    const topOpenings = getGroupTopOpenings(groupElem);

    return bruteforceLeft(groupElem, topOpenings);
}

const solve = () => {
    // 14 groups of 3
    for (let i = 0; i < 14; i++)
        console.log(`Group ${i + 1}: ${bruteforceGroup(i) ? "Passed" : "Failed"}`);
}

solve();
