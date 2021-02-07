import React, { Component } from 'react';

import InputBox from './inputBox.js';
import SubmitButton from './submitButton.js';
import StatBox from '../statBox.js';

import title_styles from  './Styling/title.module.css'
import submitBorder from './Styling/submitBorder.module.css'
import similarTweetStyle from './Styling/similarTweets.module.css'

import { get_headers } from '../sharedAPIs.js'
import { get_recent_tweets,
         get_from_username,
         post_create_text,
         get_text_analyzer,
         get_if_user_exists} from './api.js'

class TwitterPage extends Component {

    constructor(props) {
        super(props);

        this.state = {
            submitted: false,
            username: "",
            data: undefined,
            top_users: [],
        };

        this.update_username = this.update_username.bind(this);
        this.submit_username = this.submit_username.bind(this);

    }

    update_username(username) {
        console.log(this.state.username_exists);
        get_if_user_exists(username)
            .then(response => this.setState({
                username: username,
                username_exists: response.data.result,
            }));

    }

    top_users_to_text(){
        let names = this.state.top_users.map(item => "@"+item[0]);
        console.log(names);
        console.log(names.join(", "));
        return names.join(", ");
    }

    update_data(new_data) {
        this.setState({
            submitted: true,
            data: {
                rows: [new_data.report],
            },
            top_users: new_data.result.slice(0, 3),
        });
    }

    handle_second_response(response) {
        if(response.status === 201){
            get_text_analyzer(response.data.id)
                .then(next_response => this.update_data(next_response.data));
        } else {
            console.log("An error occurred with the following response:");
            console.log(response);
        }

    }

    handle_response(response) {
        if(response.status === 208){
            get_text_analyzer(response.data.existing_id)
            .then(next_response => this.update_data(next_response.data));
        } else if(response.status === 200) {
            post_create_text(response.data)
                .then(response => this.handle_second_response(response))
                .catch(error => console.log(error))
        }
    }

    submit_username() {

        get_from_username(this.state.username)
            .then(response => this.handle_response(response))
            .catch( error => console.log(error));

    }


    render() {
        let results;

        if(this.state.submitted){
            results = (<div>
            <StatBox get_headers={get_headers}
                         data={this.state.data}
                         title={"Tweet Statistics"}
                />
                <div className={similarTweetStyle.default}>
                    <h3>{"Similar Tweeters:"} </h3>
                    <h5>{this.top_users_to_text()}</h5>
                </div>
        </div>);
        } else {
            results = (<div>{}</div>)
        }



        return (
            <div>
                <h1 className={title_styles.default}> Twitter-Analyzer </h1>
                <div className={submitBorder.default}>
                <InputBox onChange={this.update_username}
                          userExists={this.state.username_exists}/>
                <SubmitButton onClick={this.submit_username}/>
                </div>
                {results}
            </div>
        );
    }
}


export default TwitterPage;