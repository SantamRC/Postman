var path=require('path');

module.exports={
    mode:'development',
    entry:path.join(__dirname,'./src/app.js'),
    output:{
        path:path.join(__dirname,'public'),
        filename: 'index.js'
    },
    module:{
        rules:[
            {
                test: /\.js/,
                exclude: /node_modules/,
                use: 'babel-loader'
            }
        ]
    }
}