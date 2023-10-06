import { getUsers, deleteUserById, getUserById } from './../db/users';
import express from 'express';


export const getAllUsers = async (req: express.Request, res: express.Response) => {
    try {
        const users = await getUsers()
        return res.status(200).json(users);
    } catch (error) {
        console.log(error);
        return res.sendStatus(400);
    }
}

export const deleteUser = async (req: express.Request, res: express.Response) => {
    try {
        const { id } = req.params;

        const deletedUser = await deleteUserById(id);

        return res.status(200).json(deletedUser);
    } catch (error) {
        console.log(error);
        return res.sendStatus(400);
    }
}

export const updateUser = async (req: express.Request, res: express.Response) => {
    try {
        const { id } = req.params;
        const { username } = req.body;

        if (!username) {
            return res.sendStatus(400);
        }

        const user = await getUserById(id);

        if (!user) {
            return res.sendStatus(404);
        }

        user.username = username;
        await user.save();

        return res.status(200).json(user);

    } catch (error) {
        console.log(error);
        return res.sendStatus(400);
    }
}