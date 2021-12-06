<template>
  <section>
    <div class="container mx-auto">
      <div class="min-h-screen"> 
      <div class="grid grid-cols-2 md:grid-grid-cols-3 lg:grid-cols-5 grid-rows-2 gap-3 p-2">
        <div class="col-start-1 bg-gray-100 text-gray-500 text-lg font-bold text-center p-10 rounded-lg">15 Total Listings</div> 
        <div class="col-start-2 col-span-4 row-start-1 row-end-3 bg-gray-100 text-gray-500 text-lg font-bold text-center p-10 rounded-lg">
          <p>Positions Density</p>
          <div class="grid place-items-center pt-10">
          <!-- <PieGraph :pieData="pieData"/>  -->
          </div>
        </div>
        <div class="relative col-start-2 col-span-4 row-start-3 row-end-6 bg-gray-100 text-gray-500 text-lg font-bold text-center p-10 rounded-lg">
          <p>Pending Listings</p>
            <PendingListingModule/>
         
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
//  import PieGraph from "./PieGraph.vue";
 import PendingListingModule from "./PendingListingModule.vue";
export default {
  name: "AdminDashboard",
   
  // data:() => { 
  //    return { 
  //      pieData: [
  //        {color: "#0B6487", value: 30}, 
  //        {color: "#9D1F37", value: 40}, 
  //        {color: "#F6931C", value: 30}

  //      ]
  //    };
  //  },

  components: {
    //  PieGraph,
     PendingListingModule,
   }
};
</script>
