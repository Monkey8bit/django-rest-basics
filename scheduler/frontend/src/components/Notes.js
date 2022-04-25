import React, {useState, useEffect} from "react";
import axios from "axios";
import {useParams} from "react-router-dom";


const NoteItem = ({note}) => {
    return (
        <tr key={note.note_id}>
            <td>{note.note_id}</td>
            <td>{note.user_created}</td>
            <td>{note.description}</td>
            <td>{note.created}</td>
            <td>{note.is_active.toString()}</td>
        </tr>
    )
}

const NotesList = () => {
    const [notes, setNotes] = useState([]);
    const [project, setProject] = useState({})
    const id = useParams().id;

    useEffect(() => {
        const Project = () => {
            axios
                .get(`http://127.0.0.1:8000/api/projects/?project_id=${id}`)
                .then(response => setProject(response.data[0]))
                .catch(error => console.log(error));
        }
        Project();
    }, [id])

    useEffect(() => {
        const ProjectNotes = () => {
            axios
                .get(`http://127.0.0.1:8000/api/projects/${id}`)
                .then(response => setNotes(response.data))
                .catch(error => console.log(error));
        }
        ProjectNotes();
    }, [id]);
    return (

        [
            <div className={"project_header"}>Project name: <strong>{project.name}</strong></div>,
            <table className={"maintable notelist"}>
                <th>Id</th>
                <th>User created</th>
                <th>Description</th>
                <th>Created at</th>
                <th>Is active</th>
                {notes.map((note) => <NoteItem note={note} />)}
            </table>
        ]
    );
};

export default NotesList