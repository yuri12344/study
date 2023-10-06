import mongoose from "mongoose";

const userSchema = new mongoose.Schema({
    username: { type: String, unique: true, required: true },
    email: { type: String, unique: true, required: true },
    authentication: {
        password: { type: String, required: true, select: false },
        salt: { type: String, select: false },
        sessionToken: { type: String, select: false }
    }
});

export const UserModel = mongoose.model("User", userSchema);

export const getUsers = () => UserModel.find()
export const getUserByEmail = (email: string) => UserModel.findOne({ email })
export const getUserBySessionToken = (sessionToken: string) => UserModel.findOne({ "authentication.sessionToken": sessionToken })
export const getUserById = (userId: string) => UserModel.findById(userId)
export const createUser = (values: Record<string, any>) => UserModel.create(values).then((user: any) => user.toObject())
export const deleteUserById = (id: string) => UserModel.findByIdAndDelete(id)
export const updateUserById = (id: string, values: Record<string, any>) => UserModel.findByIdAndUpdate(id, { $set: { ...values } }, { new: true }).then((user: any) => user.toObject())
