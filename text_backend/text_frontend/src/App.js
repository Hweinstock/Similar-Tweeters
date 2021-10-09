import React, { Component } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from '@material-ui/core/Button';

import navStyles from "./navBar.module.css";

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import TextBoxPage from "./Component/TextBoxPage/index.js";
import TwitterPage from "./Component/TwitterPage/index.js";


export default function App() {
  return (
      <Router>
        <div>
          <nav>
                <div className={navStyles.navBar}>
                    <Button className={navStyles.pageLink} style={{ fontSize: '20px', border: '2px solid', borderRadius: '0px'}} component={Link} to="/">
                    Text Boxes
                    </Button>
                    <Button className={navStyles.pageLink} style={{ fontSize: '20px', border: '2px solid', borderRadius: '0px'}} component={Link} to="/twitter">
                    Twitter
                    </Button>
                </div>
          </nav>

          <Switch>
            <Route path="/twitter">
                <TwitterPage/>
            </Route>
            <Route path="/">
                <TextBoxPage/>
            </Route>
          </Switch>
        </div>
      </Router>
  );
}
