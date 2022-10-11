module.exports = (req, res) => {
    if (req.method === 'GET'){
        res.json([
            {text: "Success!"}
        ])
    } else {
        const {text} = req.body;
        res.send({status: "Command recieved", text});
    }
}