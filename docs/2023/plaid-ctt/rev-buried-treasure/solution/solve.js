import fs from "fs";
import http from "http";

const fsp = fs.promises;

async function download(url, filePath) {
    const file = fs.createWriteStream(filePath);

    return new Promise((resolve, reject) => {
        http.get(url, (response) => {
            response.pipe(file);
            file.on("finish", () => {
                file.close();
                resolve();
            });
        }).on("error", (err) => {
            fs.unlink(filePath);
            reject(err);
        });
    });
}

const prepare = async () => {
    for (let i = 0; i < 200; i++) {
        const jsFile = `${i}.js`;
        const jsMapFile = `${i}.js.map`;
        if (!fs.existsSync(jsFile))
            await download(`http://treasure.chal.pwni.ng/${jsFile}`, jsFile);
        if (!fs.existsSync(jsMapFile))
            await download(`http://treasure.chal.pwni.ng/${jsMapFile}`, jsMapFile);
    }
}

const solve = async () => {
    const b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    const result = [];

    const helper = async (target) => {
        if (result.length == 25)
            return;

        // iterate all possible indexes
        for (let i = 199; i >= 0; i--) {
            // first char starts with 0.js (edge case)
            if (result.length == 24 && i != 0)
                continue;

            // iterate all printable chars
            for (let j = 32; j < 127; j++) {
                const window = {};
                window.buffer = "AAAA".split("");
                window.buffer[0] = String.fromCharCode(j);

                const bti = b64.trim().split("").reduce((acc, x, i) => (acc.set(x, i), acc), new Map());
                const upc = window.buffer.shift();
                const moi = await fsp.readFile(`${i}.js`, "utf8");
                const tg = JSON.parse(await fsp.readFile(moi.slice(moi.lastIndexOf("=") + 1), "utf8"));
                const fl = tg.mappings.split(";").flatMap((v, l) => v.split(",").filter((x) => !!x).map((input) => input.split("").map((x) => bti.get(x)).reduce((acc, i) => (i & 32 ? [...acc.slice(0, -1), [...acc.slice(-1)[0], (i & 31)]] : [...acc.slice(0, -1), [
                    [...acc.slice(-1)[0], i].reverse().reduce((acc, i) => (acc << 5) + i, 0)
                ]].map((x) => typeof x === "number" ? x : x[0] & 0x1 ? (x[0] >>> 1) === 0 ? -0x80000000 : -(x[0] >>> 1) : (x[0] >>> 1)).concat([
                    []
                ])), [
                    []
                ]).slice(0, -1)).map(([c, s, ol, oc, n]) => [l, c, s ?? 0, ol ?? 0, oc ?? 0, n ?? 0]).reduce((acc, e, i) => [...acc, [l, e[1] + (acc[i - 1]?.[1] ?? 0), ...e.slice(2)]], [])).reduce((acc, e, i) => [...acc, [...e.slice(0, 2), ...e.slice(2).map((x, c) => x + (acc[i - 1]?.[c + 2] ?? 0))]], []).map(([l, c, s, ol, oc, n], i, ls) => [tg.sources[s], moi.split("\n").slice(l, ls[i + 1] ? ls[i + 1]?.[0] + 1 : undefined).map((x, ix, nl) => ix === 0 ? l === ls[i + 1]?.[0] ? x.slice(c, ls[i + 1]?.[1]) : x.slice(c) : ix === nl.length - 1 ? x.slice(0, ls[i + 1]?.[1]) : x).join("\n").trim()]).filter(([_, x]) => x === upc).map(([x]) => x)?.[0] ?? tg.sources.slice(-2, -1)[0];
                if (fl === `${target}.js`) {
                    // console.log(`file idx: ${i}, char: ${String.fromCharCode(j)}`);
                    result.push(String.fromCharCode(j));
                    await helper(i);
                    return;
                }
            }
        }
    }

    await helper("success");
    console.log(`PCTF{${result.reverse().join("")}}`);
}

(async () => {
    console.log("Preparing environment...");
    await prepare();
    console.log("Solving...")
    await solve();
    // Need+a+map/How+about+200!
})();
