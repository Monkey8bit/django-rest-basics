import React from "react";
import "./App.css";
import axios from "axios";
import UserList, {SingleUser} from "./components/User";
import ProjectList from "./components/Projects";
import NotesList from "./components/Notes";
import {BrowserRouter, Route, Routes, Link} from "react-router-dom";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            "users": [],
            "projects": [],
        }
    }

    componentDidMount() {
        axios
            .get("http://127.0.0.1:8000/api/users/")
            .then(response => {
                let users = response.data;
                this.setState({
                    "users": users
                })
            })
            .catch(error => console.log(error));
        axios
            .get("http://127.0.0.1:8000/api/projects/")
            .then(response => {
                let projects = response.data;
                this.setState({
                    "projects": projects
                })
            })
            .catch(error => console.log(error));
    };
    render() {
        return (
            <div className={"container"}>
                <div className={"menu"}>
                    <ul className={"navbar"}>
                        <li><a href="/">Lorem ipsum.</a></li>
                        <li><a href="/">Lorem.</a></li>
                        <li><a href="/">Lorem ipsum dolor.</a></li>
                    </ul>
                </div>
                <BrowserRouter>
                    <nav>
                        <li><Link to="users">Users</Link></li>
                        <li><Link to="projects">Projects</Link></li>
                    </nav>
                    <Routes>
                        <Route exact path="users" element = {<UserList users={this.state.users} />} />
                        <Route exact path="projects" element = {
                            <ProjectList projects={this.state.projects}/>
                        } />
                        <Route path="projects/:id" element = {<NotesList />} />
                        <Route path="users/:id" element = {<SingleUser />} />
                    </Routes>
                </BrowserRouter>
                <div className={"footer"}>
                    <p>2022 &copy; GB Scheduler </p>
                </div>
            </div>
        )
    };
}


export default App;
