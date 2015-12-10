/**
 Design Patterns v1

 Design -> Creational -> Singleton
 JavaScript
 Daniel Vega Ceja, 2015
**/

var mySingleton = (function () {
   // Instance stores a reference to the Singleton.
  var instance;

  function init() {
    // Private methods and variables.
    function privateMethod(){
        console.log( "I am private" );
    }
    var privateRandomNumber = Math.round(Math.random()*1000);

    return {
      // Public methods and variables.
      publicMethod: function () {
        privateMethod();
        console.log( "Public scope can see me!" );
      },
      publicProperty: "I am also public",
      getRandomNumber: function() {
        return privateRandomNumber;
      }
    };

  };

  return {
    // Get the Singleton instance if one exists
    // Create one if it doesn't
    getInstance: function () {
      if ( !instance ) {
        instance = init();
      }
      return instance;
    }
  };

})();

// Implementation:

var singleA = mySingleton.getInstance();
var singleB = mySingleton.getInstance();
//singleA.publicMethod();
//singleA.privateMethod();
console.log( singleB.getRandomNumber() );
console.log(" It's the same? -> " + (singleA.getRandomNumber() === singleB.getRandomNumber()) ); // true
