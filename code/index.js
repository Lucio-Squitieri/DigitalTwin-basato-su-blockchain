const Moralis = require('moralis').default
const fs = require('fs')
require('dotEnv').config()

const fileUploads = [
  {
    path: 'modello.json',
    content: fs.readFileSync(
      '/Users/luciosquitieri/Documents/parameters.json',
      {
        encoding: 'base64',
      }
    ),
  },
]

async function uploadToIpfs() {
  await Moralis.start({
    apiKey: process.env.MORALIS_KEY,
  })

  const res = await Moralis.EvmApi.ipfs.uploadFolder({
    abi: fileUploads,
  })

  console.log(res.result)
}

uploadToIpfs()
