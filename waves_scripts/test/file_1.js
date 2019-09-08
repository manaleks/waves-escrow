const wvs = 10 ** 8;

const dApp = "3MvqUEAdK8oa1jDS82eqYYVoHTX3S71rRPa";
const sellerSeed = "verb venue bullet valley impact speak column renew toddler actress ankle mandate";
const sellerPublicKey = "ANLvS9cUXfiHVkxyrfhPuJUWnPrALiWiXhaEaqkNb86h";
const sellerAddress = "3MwrdZXvzCCsYHCYDKWMTZMkGfNHUPvY9K6";
const buerSeed = "donkey cannon enforce front wedding coast song inherit banana ticket kiss maximum";

const sellerAddress2 = "3N1Am2HYx2r1e2rSAegRJxRmWwuUMFmvUXx";
const sellerSeed2 = "blouse crime bless negative much entire swear like feed ladder endorse sphere";

const homeId = "16"

describe('wallet test suite', async function () {
    this.timeout(100000);

    it('sethome', async function () {
        const invoke = invokeScript({
            dApp,
            call: {
                function: "sethome",
                args: [{"type": "string", "value": homeId}]
            },
            payment: null,
        }, sellerSeed2);

        await broadcast(invoke);
        await waitForTx(invoke.id);
    });

    it('main', async function () {
        const invoke = invokeScript({
            dApp,
            call: {
                function: "main",
                args: [
                    {"type": "string", "value": homeId},
                    {"type": "string", "value": sellerAddress2},
                ],
            },
            payment: [{amount: 1 * wvs}],
        }, buerSeed);

        await broadcast(invoke);
        await waitForTx(invoke.id);
    });
});