module.exports = {
  lintOnSave: false,
  chainWebpack: (config) => {
    config.module
      .rule("json")
      .test(/\.json$/)
      .use("json-loader")
      .loader("json-loader")
      .end();
  },
};
