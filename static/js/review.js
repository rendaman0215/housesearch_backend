var vm = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'], //デリミタの変更
    data: {
        id: location.href.split('/').pop(),
        reviews: [],
    },
    mounted: function() {
      axios.get('/api/reviews/' + id)
        .then(function (response) {
          for(var d in response.data) {
            var item = response.data[d];
            item.due = new Date(item.due);
            vm.reviews.push(item);
          }
        })
      .catch(function (error) {
        console.log(error);
      })
      .then(function () {
      });
    },
});