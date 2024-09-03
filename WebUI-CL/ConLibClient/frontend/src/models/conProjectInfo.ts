import { ConProject } from 'connection-restapi-client-poc';


export interface  OpenProjectResult {
    openClientId : string | null;
    openProjectId : string | null;
    projectInfo : ConProject | null
}
