export default class Building {
    constructor(sqft) {
        this.sqft = sqft

        // this.constructor !== Building checks "are we in a child class?"
        // typeof this.evacuationWarningMessage !== 'function' checks "is the method missing?"
        // if both are true, throw the error
        if (this.constructor !== Building && typeof this.evacuationWarningMessage !== 'function') {
        throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    }

    get sqft() {
        return this._sqft;
    }

    set sqft(value) {
    if (typeof value !== 'number') {
        throw new TypeError('Sqft must be a number');
    }
    this._sqft = value;
    }
}
