export default function createInt8TypedArray(length, position, value) {
    const buffer = new ArrayBuffer(length);
    const newArr = new Int8Array(buffer);

    if (position < 0 || position >= length) {
        throw new Error("Position outside range");
    } else {
        newArr[position] = value;
        return new DataView(buffer);
    }
}
