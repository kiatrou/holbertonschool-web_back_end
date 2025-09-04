function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      // Log for every resolution (success case)
      console.log('Got a response from the API');
      
      // Return object when Promise resolves
      return {
        status: 200,
        body: 'success'
      };
    })
    .catch(() => {
      // Log for every resolution (including rejections)
      console.log('Got a response from the API');
      
      // Return empty Error object when Promise rejects
      return new Error();
    });
}
