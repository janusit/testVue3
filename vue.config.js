const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

// module.exports = {
//   devServer: {
//     proxy: {
//       '/src': {
//         target: 'http://localhost:8080',
//         pathRewrite: { '^/src': '' },
//         bypass: function(req, res) {
//           if (req.path.endsWith('.json')) {
//             return `/src${req.path}`;
//           }
//         }
//       }
//     }
//   }
// }
