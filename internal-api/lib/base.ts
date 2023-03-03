import { Deta } from "detajs-sm";

const deta = Deta();

const libDB = deta.Base("library");

export { libDB };
