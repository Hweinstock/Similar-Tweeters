import axios from "axios";

export function get_recent_tweets(username){
    let params = {
            params: {
                username: username,
            }
    };

    return axios.get('/api/twitter/recent', params)
}


export function get_and_post_username(username){
    let get_data = {
        params: {
            username: username,
        },
    };

    let result = axios.get('/api/fromUsername/', get_data)
        .then(response => create_text_object(response.data))
        .catch( error => console.log(error));

    return result

}

function create_text_object(post_data){
    console.log(post_data);

    let sec_response = axios.post('/api/text/', post_data)
            .then(sec_response => console.log(sec_response))
            .catch(error => console.log(error))

}



export default { get_recent_tweets, get_and_post_username }
