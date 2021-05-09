var vm = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'], //デリミタの変更
    data: {
        makers: [],
    },
    mounted: function() {
      axios.get('/api/makers/')
        .then(function (response) {
          for(var d in response.data) {
            var item = response.data[d];
            item.due = new Date(item.due);
            vm.makers.push(item);
          }
        })
      .catch(function (error) {
        console.log(error);
      })
      .then(function () {
      });
    },
});