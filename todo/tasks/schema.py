import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from tasks.models import Task


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        filter_fields = ['id', 'name']
        interfaces =(graphene.relay.Node,)


class Query(graphene.ObjectType):
    task = graphene.relay.Node.Field(TaskType)
    task_list = DjangoFilterConnectionField(TaskType)



class TaskMutation(graphene.relay.ClientIDMutation):
    class Input:
        id=graphene.UUID(required=False)
        name=graphene.String(required=True)
        subject=graphene.String(required=True)
        detail = graphene.String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        id = input.get('id')
        task = Task.objects.get(id=id)
        if task is None :
            task = Task()

        for k, v in input.items():
            setattr(task, k, v)

        task.save()
        return cls(task)


class TaskDeleteMutation(graphene.relay.ClientIDMutation):
     class Input:
         id = graphene.UUID(required=False)

     @classmethod
     def mutate_and_get_payload(cls, root, info, **input):
        id= input.get('id')
        task = Task.objects.get(id=id)
        task.delete()
        return cls(instance=task)


class Mutation(graphene.ObjectType):
    task = TaskMutation.Field()
    delete_task = TaskDeleteMutation.Field()


schema = graphene.Schema(query=Query,mutation=Mutation)