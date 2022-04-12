<template>
  <section>
    <div class="container mx-auto">
      <div class="min-h-screen"> 
      <div class="grid grid-cols-2 md:grid-grid-cols-3 lg:grid-cols-5 grid-rows-2 gap-3 p-2">
        <div class="col-start-1 bg-gray-100 text-gray-500 text-lg font-bold text-center p-10 rounded-lg">15 Total Listings</div> 
        <div class="relative col-start-2 col-span-8 row-start-1 row-end-4 bg-gray-100 text-gray-500 text-lg font-bold text-center p-10 rounded-lg place-content-center">
          <div class="flex flex-start ">
            <div class="mx-auto my-auto py-4" style="height:13vh; width:23vw;">
            Views by Job Type 
              <div>
                <vue3-chart-js
                    :id="viewsChart.id"
                    :type="viewsChart.type"
                    :data="viewsChart.data"
                    @before-render="beforeRenderLogic"
                ></vue3-chart-js>
              </div>
            </div>

            <div class="mx-auto my-auto py-4" style="height:13vh; width:23vw;">
            Listings by Job Type 
              <div>
                <vue3-chart-js
                    :id="listingsChart.id"
                    :type="listingsChart.type"
                    :data="listingsChart.data"
                    @before-render="beforeRenderLogic"
                ></vue3-chart-js>
              </div>
            </div>
            
          </div>
        </div>
        <div class="relative col-start-2 col-span-8 row-start-4 row-end-6 bg-gray-100 text-gray-500 text-lg font-bold text-center p-10 rounded-lg overflow-hidden pb-5 ">
          <div class="my-auto center flex-wrap">
            Site Vists and New Listings
            <div class="mx-auto my-auto" style="height:13vh; width:30vw;">
                <vue3-chart-js
                    :id="lineChart.id"
                    :type="lineChart.type"
                    :data="lineChart.data"
                    @before-render="beforeRenderLogic"
                ></vue3-chart-js>
              </div>
          </div>

        </div>
        <div class="col-start-1 row-start-2 bg-gray-100 text-gray-500 text-lg font-bold text-center p-10 rounded-lg">Most Viewed Company</div>
        <div class="col-start-1 row-start-3 bg-gray-100 text-gray-500 text-lg font-bold text-center p-10 rounded-lg">Software Engineer: Most Viewed Position</div>
        <div class="col-start-1 row-start-4 bg-gray-100 text-gray-500 text-lg font-bold text-center p-10 rounded-lg">20 Total Monthly Visits</div>
        <div class="col-start-1 row-start-5 bg-gray-100 text-gray-500 text-lg font-bold text-center p-10 rounded-lg">5 Pending Contact Requests</div>
        
      </div>
      </div>
    </div>
  </section>
</template>

<script>
 import PendingListingModule from "./PendingListingModule.vue"
 import ContactInboxModule from "./ContactInbox.vue"
 import Vue3ChartJs from '@j-t-mcc/vue3-chartjs'
 import zoomPlugin from "chartjs-plugin-zoom";
 import dataLabels from "chartjs-plugin-datalabels";
 
 Vue3ChartJs.registerGlobalPlugins([zoomPlugin]);

  export default {
    name: "AdminDashboard",
    components: {
      Vue3ChartJs,
      PendingListingModule,
      ContactInboxModule
    },
    setup () {
      const viewsChart = {
        id: 'doughnut',
        type: 'doughnut',
        data: {
          labels: ['Software Engineering', 'Machine Learning', 'Data Science', 'Robotics', 'Cyber Security'],
          datasets: [
            {
              backgroundColor: [
                '#41B883',
                '#E46651',
                '#00D8FF',
                '#DD1B16',
                '#fdfd96'
              ],
              data: [10, 9, 5, 3, 2]
            }
          ]
        }
        
      }
      const listingsChart = {
        id: 'doughnut',
        type: 'doughnut',
        data: {
          labels: ['Software Engineering', 'Machine Learning', 'Data Science', 'Robotics', 'Cyber Security'],
          datasets: [
            {
              backgroundColor: [
                '#E46651',
                '#00D8FF',
                '#41B883',
                '#fdfd96',
                '#DD1B16'
                
              ],
              data: [7, 3, 10, 2, 6]
            }
          ]
        }
        
      }
      const lineChart = {
        type: "line",
        // locally registered and available for this chart
        plugins: [dataLabels],
        data: {
          labels: [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
          ],
          datasets: [
            {
              label: "New Listings",
              data: [15, 13, 14, 10, 5, 3, 4, 9, 15, 20, 25, 22],
              fill: false,
              borderColor: "#41B883",
              backgroundColor: "black",
            },
            {
              label: "Site Visits",
              data: [20, 28, 41, 35, 30, 10, 15, 10, 25, 30, 22, 35],
              fill: false,
              borderColor: "#00D8FF",
              tension: 0.5,
              backgroundColor: "blue",
            },
          ],
        },
        options: {
          plugins: {
            zoom: {
              zoom: {
                wheel: {
                  enabled: true,
                },
                pinch: {
                  enabled: true,
                },
                mode: "y",
              },
            },
            datalabels: {
              backgroundColor: function (context) {
                return context.dataset.backgroundColor;
              },
              borderRadius: 4,
              color: "white",
              font: {
                weight: "bold",
              },
              formatter: Math.round,
              padding: 6,
            },
            title: {
                display: true,
                text: 'Custom Chart Title',
                padding: {
                    top: 10,
                    bottom: 30
                }
            },
          },
        },
      };
    
      const beforeRenderLogic = (event) => {
        //...
        //if(a === b) {
        //  event.preventDefault()
        //}   
      }    

      return {
        viewsChart,
        listingsChart, 
        lineChart,
        beforeRenderLogic
      }
    }
  };
</script>

