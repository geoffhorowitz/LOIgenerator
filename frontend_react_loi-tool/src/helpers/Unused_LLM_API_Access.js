const express = require('express') //helps to make endpoints available
const axios = require('axios')
const app = express()
const {HfInference} = require('@huggingface/inference')

app.use(express.urlencoded({extended: true}))
app.use(express.json())

app.post('text2image', 
    async (req, res) => {
        const {
            token,
            model = 'prompthero/openjourney-v4', //can use any default model, eg runwayml/stable-diffusion-v1-5
            prompt, //only fully required input
            parameters,
        } = req.body

        if (!prompt) {
            return res.status(400).send('Missing required parameters: prompt')
        }

        const inference = new HfInference(token)

        try {
            const blob = await inference.textToImage({
                model: model,
                inputs: prompt,
                parameters: parameters,
                })
            const buffer = await blob.arrayBuffer()
            const base64data = Buffer.from(buffer).toString('base64')
            const img = `data:${blob.type};base64data,${base64data}`

            res.json({buffer: img })
        } catch (error) {
            console.error(error)
            res.status(500).send(`Error generating the image: ${error.message}`)
        }
    }
)

// start the server
const port = 3600
app.listen(port, () => {
    console.log(`Server started on port ${port}`)
})

/*
if running locally, can use ngrock to run test
Terminal 1: node <thisfile>.js
Terminal 2: ngrok http <port_value> (e.g. 3600)
will get post url https://<abunchofvalues>.ngrok.free.app
to use in POST method, append the post endpoint above (e.g. /text2image) 
--> URL: https://<abunchofvalues>.ngrok.free.app/text2image
--> Content-Type: application/json
--> Body: {"prompt": <prompt value>, <any_other_paramters_wanted>: <see above>}

will return a dictionary with the image data in {"buffer": ....}
*/