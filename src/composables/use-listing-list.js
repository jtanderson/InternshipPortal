import { ref, toRefs, reactive } from "vue";
import useFetch from "./use-fetch";
export default function () {
  let listings = reactive({ list: [], error: null, fetching: false });
  const val = ref("");
  const submitted = async () => {
    const { response, error, fetchData, fetching } = useFetch(
      `${process.env.SERVER_URL}/admin/get-listings/pending`
    );
    fetchData();
    listings.list = response;
    listings.error = error;
    listings.fetching = fetching;
  };
  return { submitted, ...toRefs(listings), val };
}
