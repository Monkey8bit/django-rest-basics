import React from "react";
import {Link} from "react-router-dom";


const ProjectItem = ({project}) => {
    console.log(project)
    let users = project.users.map((user) => <li>{user}</li>)
    return (
        <tr key={project.project_id}>
            <td>{project.project_id}</td>
            <td><Link to={`/projects/${project.project_id}`}>{project.name}</Link></td>
            <td>{project.description}</td>
            <td>{project.link}</td>
            <td>
                <ul>
                    {users}
                </ul>
            </td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table className={"maintable projectlist"}>
            <th>Id</th>
            <th>Name</th>
            <th>Description</th>
            <th>Link</th>
            <th>Users</th>
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList
export {ProjectItem}
