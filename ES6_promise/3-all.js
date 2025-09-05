import { uploadPhoto, createUser } from "./utils.js"

export default function handleProfileSignup() {
    return Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
        const body = results[0].body;
        const firstName = results[1].firstName;
        const lastName = results[1].lastName;

        console.log(body + " " + firstName + " " + lastName);
    })

    .catch(() => {
        console.log("Signup system offline")
        return new Error();
    })
}