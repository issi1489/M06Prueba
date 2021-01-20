
/*FUNCIÓN LOGIN */

function pasuser(form) {
    if (form.id.value=="margarita" && form.pass.value=="1234") { 
                
        location="privada_paciente.html" 
      } 
    
    else if (form.id.value=="dra.elizabeth" && form.pass.value=="4321") { 
                
        location="privada_medico.html" 
      } 

    else {
        alert("Datos incorrectos, por favor vuelve a intentar")
      }
  
  }

/*--------CHARTS-----------*/

/*--------CHART INSULINA-----------*/
var years = ['ene','feb','mar','abr','may','jun','jul','ago','sept','nov','dic'];

/*--------CHART INSULINA-----------*/
var ins_2018 = [15,30,106,116,40,20,37,100,110,111,96,120];
var ins_2019 = [140,100,88,60,55,61,99,76,120,99,78,114];
var ins_2020 = [103,77,55,33,47,88,84,58,120,140];
/*--------CHART HEMOGRAMA-----------*/
var hglob_2018 = [3.3,3.9,4.3,4.6,4.55,4.77,5.6,5.2,3.8,4.2,4.8,4.99];
var hglob_2019 = [4.3,4.9,5.3,5.6,3.55,3.77,5.6,6.2,6.8,6.2,5.8,3.99];
var hglob_2020 = [4.9,4.1,5.7,6.6,6.55,5.77,4.6,4.2,4.8,2.2,4.8,4.99];

var hhemo_2018 = [11,13,16,17,15,13.4,15.1,17,15.2,14.8,13.5,12.5];
var hhemo_2019 = [12.9,11,15.2,14.8,13.5,17,15,13.4,15.1,11,13,16];
var hhemo_2020 = [17,15,13.4,15.1,15.2,14.8,13.5,13.4,15.1,17];

var hhema_2018 = [33,30,45,50,40,20,37,22,37,40,45,38];
var hhema_2019 = [37,22,37,40,55,61,20,37,20,29,38,54];
var hhema_2020 = [45,50,40,20,47,38,44,48,40,36];

var hrdw_2018 = [15,11,10,16,13,12,11.5,12.3,13.1,13.9,14,13.5];
var hrdw_2019 = [14,10,18,15,18.5,20,18.3,15.8,12.1,13.6,14.8,11.4];
var hrdw_2020 = [16,13,12,11.5,12.8,12.1,13.6,16,13,12];




var ctx = document.getElementById("myChart_insulina");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
        { 
            data: ins_2018,
            label: "2018",
            borderColor: "#2af8c0",
            fill: false
          },
          { 
            data: ins_2019,
            label: "2019",
            borderColor: "#2a43f8",
            fill: false
          },
          { 
            data: ins_2020,
            label: "2020",
            borderColor: "#c02af8",
            fill: false
          }
          
          
    ]
  }
});

var ctx = document.getElementById("myChart_Hemograma1");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
        { 
            data: hglob_2018,
            label: "2018",
            borderColor: "#f8562a",
            fill: false
          },
          { 
            data: hglob_2019,
            label: "2019",
            borderColor: "#62f82a",
            fill: false
          },
          { 
            data: hglob_2020,
            label: "2020",
            borderColor: "#2af8d3",
            fill: false
          }
          
          
    ]
  }
});

var ctx = document.getElementById("myChart_Hemograma2");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
        { 
            data: hhemo_2018,
            label: "2018",
            borderColor: "#c659c0",
            fill: false
          },
          { 
            data: hhemo_2019,
            label: "2019",
            borderColor: "#59c3c6",
            fill: false
          },
          { 
            data: hhemo_2020,
            label: "2020",
            borderColor: "#5cc659",
            fill: false
          }
          
          
    ]
  }
});

var ctx = document.getElementById("myChart_Hemograma3");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
        { 
            data: hhema_2018,
            label: "2018",
            borderColor: "#0c797c",
            fill: false
          },
          { 
            data: hhema_2019,
            label: "2019",
            borderColor: "#d95f00",
            fill: false
          },
          { 
            data: hhema_2020,
            label: "2020",
            borderColor: "#d9cc00",
            fill: false
          }
          
          
    ]
  }
});

var ctx = document.getElementById("myChart_Hemograma4");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
        { 
            data: hrdw_2018,
            label: "2018",
            borderColor: "#be2222",
            fill: false
          },
          { 
            data: hrdw_2019,
            label: "2019",
            borderColor: "#0c7c35",
            fill: false
          },
          { 
            data: hrdw_2020,
            label: "2020",
            borderColor: "#0c2b7c",
            fill: false
          }
          
          
    ]
  }
});



