using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfApp1_TaskHandler
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private ObservableCollection<Task> Tasks { get; set; } = new ObservableCollection<Task>();

        public MainWindow()
        {
            InitializeComponent();
            Tasks = new ObservableCollection<Task>();
            taskListView.ItemsSource = Tasks;
        }

        private void AddTask_Click(object sender, RoutedEventArgs e)
        {
            AddEditTaskWindow addWindow = new AddEditTaskWindow();
            if (addWindow.ShowDialog() == true)
            {
                Tasks.Add(addWindow.Task);
                taskListView.ItemsSource = Tasks;
            }
        }
        private void EditTask_Click(object sender, RoutedEventArgs e)
        {
            if (taskListView.SelectedItem is Task selectedTask)
            {
                // Open a window to edit the selected task
                AddEditTaskWindow editWindow = new AddEditTaskWindow();
                if (editWindow.ShowDialog() == true)
                {
                    int index = Tasks.IndexOf(selectedTask);
                    Tasks[index] = editWindow.Task;
                }
            }
        }

        private void DeleteTask_Click(object sender, RoutedEventArgs e)
        {
            if (taskListView.SelectedItem is Task selectedTask)
            {
                // Confirm the deletion
                MessageBoxResult result = MessageBox.Show("Are you sure you want to delete this task?", "Confirm Deletion", MessageBoxButton.YesNo, MessageBoxImage.Warning);
                if (result == MessageBoxResult.Yes)
                {
                    // Remove the task from the collection
                    Tasks.Remove(selectedTask);
                }
            }
        }
    }
}
