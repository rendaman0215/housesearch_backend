var vm = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'], //デリミタの変更
    data: {
        keyword: '',
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
    computed: {
        filteredMakers: function() {
            var makers = [];
            for(var i in this.makers) {
                var maker = this.makers[i];
                if(
                  maker.name.indexOf(this.keyword) !== -1 ||
                  maker.name_hira.indexOf(this.keyword) !== -1 ||
                  maker.name_kata.indexOf(this.keyword) !== -1 ||
                  maker.name_eng.indexOf(this.keyword) !== -1
                ) {
                    makers.push(maker);
                }
            }
            return makers;
        },
    }
});