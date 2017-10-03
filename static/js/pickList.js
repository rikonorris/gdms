(function ($) {

   $.fn.pickList = function (options, groups) {
      var opts = $.extend({}, $.fn.pickList.defaults, options);

      this.fill = function () {
         function mapCallback (value){
            var group = '';
            group += '<optgroup id=\"' + value.id + '\" label=\"' + value.text + '\"></optgroup>';
            this.find('.pickData').append(group);
         }
         groups.groups.map(mapCallback.bind(this));

         $.each(opts.data, function (key, val) {
            var option = '<option department-id=' + val.dep_id +' data-id=' + val.id + '>' + val.text + '</option>';
            $('#' + val.dep_id).append(option);
         });
      };
      this.control = function () {
         var pickThis = this;

         pickThis.find(".pAdd").on('click', function () {
            var p = pickThis.find(".pickData option:selected");
            p.clone().appendTo(pickThis.find(".pickListResult"));
            p.remove();
         });

         pickThis.find(".pAddAll").on('click', function () {
            var p = pickThis.find(".pickData option");
            p.clone().appendTo(pickThis.find(".pickListResult"));
            p.remove();
         });

         pickThis.find(".pRemove").on('click', function () {
            $(".pickListResult option:selected").map(
                function() {
                    $('#' + this.getAttribute('department-id')).append(this)
                }
            );
         });

         pickThis.find(".pRemoveAll").on('click', function () {
            $(".pickListResult option").map(
                function() {
                    $('#' + this.getAttribute('department-id')).append(this)
                }
            );
         });
      };

      this.getValues = function () {
         var objResult = [];
         this.find(".pickListResult option").each(function () {
            objResult.push({
               id: $(this).data('id'),
               text: this.text
            });
         });
         return objResult;
      };

      this.init = function () {
         var pickListHtml =
                 "<div class='row'>" +
                 "  <div class='col-sm-5'>" +
                 "	 <select class='form-control pickListSelect pickData' multiple></select>" +
                 " </div>" +
                 " <div class='col-sm-2 pickListButtons'>" +
                 "	<div class='pAdd btn btn-default btn-fill btn-wd'>" + opts.add + "</div>" +
                 "      <div class='pAddAll btn btn-default btn-fill btn-wd'>" + opts.addAll + "</div>" +
                 "	<div class='pRemove btn btn-default btn-fill btn-wd'>" + opts.remove + "</div>" +
                 "	<div class='pRemoveAll btn btn-default btn-fill btn-wd'>" + opts.removeAll + "</div>" +
                 " </div>" +
                 " <div class='col-sm-5'>" +
                 "    <select class='form-control pickListSelect pickListResult' multiple></select>" +
                 " </div>" +
                 "</div>";

         this.append(pickListHtml);

         this.fill();
         this.control();
      };

      this.init();
      return this;
   };

   $.fn.pickList.defaults = {
      add: 'Додати',
      addAll: 'Додати все',
      remove: 'Видалити',
      removeAll: 'Видалити все'
   };


}(jQuery));
