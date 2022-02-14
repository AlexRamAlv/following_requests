class RequesterCard extends HTMLElement{
    constructor(){
        super()
        
    }
    static get observedAttributes(){
        return ["img", "full-name", "position", "recived", "partial", "nonrecived", "authenticated"]
    }

    attributeChangedCallback(tag, _, newVal){
        if (tag === "img") {
            this.img = newVal;
        }
        if (tag === "full-name") {
            this.full_name = newVal;
        }
        if (tag === "position") {
            this.position = newVal;
        }
        if (tag === "recived") {
            this.recived = newVal;
        }
        if (tag === "partial") {
            this.partial = newVal;
        }
        if (tag === "nonrecived") {
            this.nonrecived = newVal;
        }
        if (tag === "edit") {
            this.edit = newVal;
        }
        if (tag === "delete") {
            this.delete = newVal;
        }
        if (tag === "authenticated") {
            if (newVal === "True"){
                this.display = "flex";
            }else{

                this.display = "none";
            }

        }

    }

    createTemplate(){
        const temp = document.createElement("template");
        temp.innerHTML = `
            <div class="requester-card">
                <img src=${this.img} alt="requester profile photo">
                <div class="user-info">
                    <h2 class="full-name">${this.full_name}</h2>
                    <p class="working-as">${this.position}</p>
                </div>
                <button class="btn btn-info" type="submit">Ver solicitudes</button>
                <div class="statistics">
                    <section class="statistics-container">
                        <div style="color: #189d00; font-weight: 500; font-size:14px">${this.recived}</div><span class="req-recived-icon"></span>
                    </section>
                    <section class="statistics-container">
                        <div style="color: #ff8d00;font-weight: 500; font-size:14px">${this.partial}</div><span class="req-partial-icon"></span>
                    </section>
                    <section class="statistics-container">
                        <div style="color: #ff0000; font-weight: 500; font-size:14px">${this.nonrecived}</div><span class="req-nonrecived-icon"></span>
                    </section>
                </div>
                
                <div class="actions" style="display:${this.display};">
                    <span id="edit-icon" class="edit-icon"></span>
                    <span class="delete-icon"></span>
                </div>
                
            </div>
        `;

        return temp
    }

    renderTemplate(){
        this.appendChild(this.createTemplate().content.cloneNode(true));
    }
    connectedCallback(){
        this.renderTemplate();
    }
}

customElements.define("requester-card", RequesterCard);