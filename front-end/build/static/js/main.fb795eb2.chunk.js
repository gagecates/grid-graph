(this["webpackJsonpgraph-app"]=this["webpackJsonpgraph-app"]||[]).push([[0],{26:function(e,t,a){},45:function(e,t,a){"use strict";a.r(t);var n=a(2),s=a.n(n),r=a(17),c=a.n(r),l=a(8),o=a.n(l),i=a(18),u=a(3),h=a(4),b=a(6),p=a(5),j=a(0),v=function(e){Object(b.a)(a,e);var t=Object(p.a)(a);function a(){var e;Object(u.a)(this,a);for(var n=arguments.length,s=new Array(n),r=0;r<n;r++)s[r]=arguments[r];return(e=t.call.apply(t,[this].concat(s))).state={buss:null,level:null},e.onBussChange=function(t){e.setState({buss:t.target.value})},e.onLevelChange=function(t){e.setState({level:t.target.value})},e.onFormSubmit=function(t){t.preventDefault(),e.state.buss<10001||e.state.buss>80100?alert("Please enter a bus number from 10001 - 80100"):console.log("ok"),0==e.state.level||null===e.state.level?alert("Please enter a level above 0"):console.log("ok"),e.props.onFormSubmit(e.state.buss,e.state.level)},e}return Object(h.a)(a,[{key:"render",value:function(){return Object(j.jsxs)("div",{className:"overview",children:[Object(j.jsx)("p",{children:"To see a focused view on a particular portion of the grid, choose a starting buss and depth level."}),Object(j.jsxs)("form",{onSubmit:this.onFormSubmit,className:"form",children:[Object(j.jsxs)("div",{className:"user-input",children:[Object(j.jsxs)("div",{className:"field",children:[Object(j.jsx)("label",{children:"Starting Buss"}),Object(j.jsx)("input",{type:"number",value:this.state.buss,placeholder:"10001-80100",onChange:this.onBussChange})]}),Object(j.jsxs)("div",{className:"field",children:[Object(j.jsx)("label",{children:"Level"}),Object(j.jsx)("input",{type:"number",value:this.state.level,onChange:this.onLevelChange})]})]}),Object(j.jsx)("button",{type:"submit",className:"button button1",children:"Fetch Graph"})]})]})}}]),a}(s.a.Component),d=function(e){var t=e.graph;return t?Object(j.jsx)("div",{className:"graph-container",children:Object(j.jsx)("img",{className:"graph",src:t,alt:"img"})}):Object(j.jsx)("div",{className:"loading",children:"Loading..."})},m=(a(26),a(19)),g=a.n(m),O=function(e){Object(b.a)(a,e);var t=Object(p.a)(a);function a(){var e;Object(u.a)(this,a);for(var n=arguments.length,s=new Array(n),r=0;r<n;r++)s[r]=arguments[r];return(e=t.call.apply(t,[this].concat(s))).state={graph:null,showGraph:!1},e.onFormSubmit=function(){var t=Object(i.a)(o.a.mark((function t(a,n){var s,r;return o.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return e.setState({graph:null}),e.setState({showGraph:!0}),t.next=4,g.a.post("https://grid-view-gmc.herokuapp.com/graph",{target:a,levels:n});case 4:s=t.sent,null===(r=s.data).image?(alert(r.message),e.setState({showGraph:!1})):e.setState({graph:r.image});case 7:case"end":return t.stop()}}),t)})));return function(e,a){return t.apply(this,arguments)}}(),e}return Object(h.a)(a,[{key:"render",value:function(){return Object(j.jsxs)("div",{children:[Object(j.jsx)("div",{className:"header",children:Object(j.jsx)("h3",{children:"Introductory Project for Frontend Engineer"})}),Object(j.jsxs)("div",{className:"main-content",children:[Object(j.jsx)(v,{onFormSubmit:this.onFormSubmit}),this.state.showGraph&&Object(j.jsx)(d,{graph:this.state.graph})]})]})}}]),a}(s.a.Component);c.a.render(Object(j.jsx)(O,{}),document.querySelector("#root"))}},[[45,1,2]]]);
//# sourceMappingURL=main.fb795eb2.chunk.js.map