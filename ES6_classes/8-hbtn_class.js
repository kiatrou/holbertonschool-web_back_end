export default class HolbertonClass {
    constructor(size, location) {
        this.size = size;
        this.locatoin = location;
    }

    get size() {
        return this._size;
    }
    set size(value) {
        if (typeof value !== "number") {
            throw new TypeError("Size must be a number")
        }
        this._size = value;
    }

    valueof() {
        return this._size;
    }

    get location() {
        return this._location;
    }
    set location(value) {
        if (typeof value !== "string") {
            throw new TypeError("Location must be a string");
        }
        this._location = value;
    }

    valueof() {
        return this._location;
    }
}
