import axios from "axios";



// async function test_call(){
//   const promise = await axios.get("http://localhost:8000/api/test");
//   const status = promise.status;
//   if(status===200)
//   {
//     return promise.data.data;
//   } else {
//       console.log("There has been an error!")
//   }
// }

const comp = {
  id: 0,
  label: 'book'
};

export function make_comparison(id) {
  return axios
      .get("/api/comps/"+id)
      // .then(response => callback_func(response))
      // .catch(error => console.log(error));
}

export function submit_texts(texts) {

  let extended_comp = comp;
  extended_comp.text1 = texts.box1;
  extended_comp.text2 = texts.box2;

  return axios
      .post("/api/comps/", comp)

  // axios
  //     .post("/api/comps/", comp)
  //     .then(response => make_comparison(response.data.id)
  //         .then(response =>))
  //     .catch(error => error);
}

export function get_headers() {
  return axios
      .get("/api/headers/")
      // .then(response => console.log(response.data))
      // .catch(error => console.log(error))
}

export function get_text_objects(text) {
  let request_data = {
    text: text,
    label: comp.label
  };
  return axios
      .post("/api/textObjects/", request_data)
      // .then(response => console.log(response.data))
      // .catch(error => console.log(error))
}

export default {submit_texts, get_headers, make_comparison, get_text_objects}