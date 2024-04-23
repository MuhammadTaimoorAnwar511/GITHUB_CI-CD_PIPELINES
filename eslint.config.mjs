import pluginReactConfig from "eslint-plugin-react/configs/recommended.js";
import globals from "globals";


export default [
  {files: ["**/*.js"], languageOptions: {sourceType: "commonjs"}},
  {languageOptions: { globals: globals.browser }},
  pluginReactConfig,
];