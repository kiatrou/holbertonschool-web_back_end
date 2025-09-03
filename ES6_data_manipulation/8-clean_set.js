export default function cleanSet(set, startString) {
    // handling edge case
    if (!startString || startString === '') {
        return '';
    }

    // converted set to array
    const arr = [...set];
    // filtered through array to find values that start with startString
    const matching = arr.filter(value => typeof value === 'string' && value.startsWith(startString));
    // removed the prefix from the values
    const withoutPrefix = matching.map(value => value.slice(startString.length));
    // joined the values with -
    const result = withoutPrefix.join('-');
    return result;
}
