export default function updateUniqueItems(map) {
    // Check if the argument is actually a Map
    if (!(map instanceof Map)) {
        throw new Error("Cannot process");
    }

    // Iterate through the map and update items with quantity 1
    for (const [key, value] of map) {
        if (value === 1) {
            map.set(key, 100);
        }
    }
    
    return map;
}
