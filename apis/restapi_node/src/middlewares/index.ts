import { getUserBySessionToken } from '../db/users';
import { NextFunction } from 'express';
import { get, merge } from 'lodash';

import express from 'express';

export const isOwner = async (req: express.Request, res: express.Response, next: NextFunction) => {
    try {
        const { id } = req.params;
        const currentuserId = get(req, 'identity.id') as string | undefined;

        if (!currentuserId) {
            return res.sendStatus(403);
        }

        if (currentuserId !== id) {
            return res.sendStatus(403);
        }
        next()
    } catch (error) {
        console.log(error);
        return res.sendStatus(400);
    }
}

export const isAuthenticated = async (req: express.Request, res: express.Response, next: NextFunction) => {
    try {
        const sessionToken = req.cookies['YURI-AUTH'];

        if (!sessionToken) {
            return res.sendStatus(401);
        }

        const existingUser = await getUserBySessionToken(sessionToken);

        if (!existingUser) {
            return res.sendStatus(401);
        }
        merge(req, { identity: existingUser });

        return next()

    } catch (error) {
        console.log(error);
        return res.sendStatus(400);
    }
}
