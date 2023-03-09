import { Deta } from "detajs-sm";
import { LibraryMangaProps } from "../typings/library";

const deta = Deta();

const libDB = deta.Base<LibraryMangaProps>("library");

export { libDB };
