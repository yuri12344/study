import express from 'express';
import http from 'http';
import bodyParser from 'body-parser';
import cookieParser from 'cookie-parser';
import compression from 'compression';
import cors from 'cors';
import mongoose from 'mongoose';

const app = express();

app.use(cors({
    credentials: true
}))

app.use(compression());
app.use(cookieParser());
app.use(bodyParser.json());

const server = http.createServer(app);

server.listen(3000, () => {
    console.log("Server is running on port http://localhost:3000")
})

const MONGO_URL = "mongodb://mongo:Silverado321@easypanel.brconnect.click:27018"

mongoose.Promise = Promise;
mongoose.connect(MONGO_URL)

mongoose.connection.on('error', (error: Error) => {
    console.log(error)
})
