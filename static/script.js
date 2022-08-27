$(".option").click(function(){
   $(".option").removeClass("active");
   $(this).addClass("active");

   setTimeout(function(chart_container) {
      let width = chart_container.width()
      let height = chart_container.height()

      chart_container.children(".chart").highcharts().setSize(width, height)
   }, 500, $(this))
});