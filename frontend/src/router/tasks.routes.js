// Composables
import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import TaskListView from "@/views/tasks/TaskListView.vue"
import NewFileView from "@/views/tasks/NewFileView.vue"

export default [
  {
    path: "/tasks",
    component: DefaultLayout,
    children: [
      {
        path: "list",
        name: "tasks-list",
        component: TaskListView,
      },
      {
        path: "new",
        name: "new-task",
        component: NewFileView,
      },
    ],
  },
]
