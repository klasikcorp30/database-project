/* Add your Application JavaScript */

$( function() {
  $( "#week").datepicker({ showAnim: "fold" });
} );

  $('#create').click(
    () => {
      swal(
        'Way To Go!',
        'You just created a meal plan',
        'success'
      )
    }
  );

  // https://api.edamam.com/search?q=desert&app_id=2fa1798f&app_key=300dd34142d127ca021b1779d7e4518e&from=0&to=3