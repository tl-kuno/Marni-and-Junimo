module.exports = (req, res) => {
    if (req.method === 'GET'){
        res.json([
            {output: "Success!"}
        ])
    } else {

    }
}