<template>
    <div>
        
    </div>
</template>

<script>

import { ref } from "vue";
export default {
    name: "MessageView",
    setup() {
        const id = ref(0);
        const message = ref("");
        const email = ref(""); 
        const name = ref("");


        return {
            id, 
            message, 
            email, 
            name,
        };
    },
};
</script>
