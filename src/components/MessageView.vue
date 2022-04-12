<template>
    <section>
        <div class="pt-28 pb-20 px-10 mx-auto my-auto">
            <div class="container shadow-md bg-gray-100 mx-auto my-auto px-10 pt-10 pb-10 text-left rounded-lg">
           
                
                <div class="block uppercase font-bold text-gray-500">Name: </div>
                    <h1 class="block text-sm font-medium text-gray-700 pb-2">
                            {{ name }}
                    </h1>
                
                <div class="block uppercase font-bold text-gray-500">Email: </div>
                    <h2 class="block text-sm font-medium text-gray-700 pb-8">
                            {{ email }}
                    </h2>
                
                <div class="block uppercase font-bold text-gray-500 pb-1">Message: 
                </div>
                    <div class="container bg-white mx-auto my-auto px-10 py-24 pt-10 pb-52 text-left rounded-lg">           
                    <p class="block text-sm font-medium text-gray-700 text-left">
                            {{ message }}
                    </p>
                    </div>   
                
                <div class="pt-5">
                 <button class="inline-flex items-center block uppercase text-gray-500 font-bold bg-white border-0 py-1 px-3 focus:outline-none hover:bg-gray-100 rounded text-base mt-4 md:mt-0" @click="toInboxPage">Back</button>   
                </div>
            </div>
        </div>

    </section>
</template>

<script>
import { ref, onMounted } from "vue";
export default {
    name: "MessageView",
    setup() {
        const id = ref(0); 
        const name = ref(""); 
        const email = ref(""); 
        const message = ref(""); 
        

        onMounted(async () =>{
            let uri = window.location.search.substring(1);
            let params = new URLSearchParams(uri);
            let message_id = params.get("id");

            let result = await fetch(
            `${process.env.SERVER_URL}/admin/get-message/${message_id}`
            ).catch((error) => {
            console.log(error);
            });
            let messages = await result.json();
      
            let m = messages.message; 
            console.log(m); 
            id.value = m.id; 
            name.value = m.name; 
            email.value = m.email; 
            message.value = m.message; 
        });
        
        function toInboxPage() {
            window.location.href = "/admin/contactinbox";
        };

        return {
            id, 
            name, 
            email, 
            message, 
            toInboxPage,
        };
    },
};
</script>
