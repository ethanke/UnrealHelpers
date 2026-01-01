"""
Mock module for the Unreal Engine Python API.
This allows tests to run in CI environments without Unreal Engine.
"""
from unittest.mock import MagicMock, PropertyMock


class MockUnrealObject:
    """Base class for mock Unreal objects."""

    def __init__(self, *args, **kwargs):
        self._properties = {}

    def set_editor_property(self, name, value):
        self._properties[name] = value

    def get_editor_property(self, name):
        return self._properties.get(name)

    def get_name(self):
        return self._properties.get('name', 'MockObject')

    def get_path_name(self):
        return self._properties.get('path', '/Mock/Path')


class MockAnimationSequence(MockUnrealObject):
    """Mock AnimationSequence class."""

    def add_notify(self, notify_class, time):
        notify = MockAnimNotify()
        notify._time = time
        return notify


class MockAnimNotify(MockUnrealObject):
    """Mock AnimNotify class."""
    pass


class MockAnimationMontage(MockUnrealObject):
    """Mock AnimationMontage class."""

    def add_section(self, name, start_time, end_time):
        section = MockMontageSection()
        section.set_editor_property('StartTime', start_time)
        section.set_editor_property('EndTime', end_time)
        return section


class MockMontageSection(MockUnrealObject):
    """Mock montage section."""
    pass


class MockBlendSpace1D(MockUnrealObject):
    """Mock BlendSpace1D class."""

    def add_animation(self, animation, position):
        return True


class MockAnimationStateMachine(MockUnrealObject):
    """Mock AnimationStateMachine class."""

    def add_state(self, state_name, animation):
        return MockState()

    def add_transition(self, from_state, to_state, transition_name):
        return MockTransition()


class MockState(MockUnrealObject):
    pass


class MockTransition(MockUnrealObject):
    pass


class MockSoundWave(MockUnrealObject):
    """Mock SoundWave class."""
    pass


class MockSoundCue(MockUnrealObject):
    """Mock SoundCue class."""

    def add_sound(self, sound_wave):
        return True


class MockSoundMix(MockUnrealObject):
    """Mock SoundMix class."""

    def add_effect(self, effect_class):
        return MockSoundEffect()


class MockSoundEffect(MockUnrealObject):
    pass


class MockSoundClass(MockUnrealObject):
    """Mock SoundClass class."""
    pass


class MockSoundAttenuation(MockUnrealObject):
    """Mock SoundAttenuation class."""
    pass


class MockWidgetBlueprint(MockUnrealObject):
    """Mock WidgetBlueprint class."""

    def add_new_widget(self, widget_class):
        return MockWidget()

    def add_new_animation(self, animation_name, length=1.0):
        anim = MockWidgetAnimation()
        anim.set_editor_property('Length', length)
        return anim


class MockWidget(MockUnrealObject):
    """Mock Widget class."""
    pass


class MockWidgetAnimation(MockUnrealObject):
    """Mock WidgetAnimation class."""

    def add_track(self, track_name, property_path):
        return MockAnimationTrack()


class MockAnimationTrack(MockUnrealObject):
    pass


class MockBlueprint(MockUnrealObject):
    """Mock Blueprint class."""

    def add_new_variable(self, var_name, var_type):
        var = MockBlueprintVariable()
        var._properties['name'] = var_name
        return var

    def add_new_function(self, function_name):
        func = MockBlueprintFunction()
        func._properties['name'] = function_name
        func.graph = MockGraph()
        return func

    def add_new_event(self, event_name):
        return MockBlueprintEvent()


class MockBlueprintVariable(MockUnrealObject):
    pass


class MockBlueprintFunction(MockUnrealObject):
    graph = None


class MockBlueprintEvent(MockUnrealObject):
    pass


class MockGraph(MockUnrealObject):
    def add_node(self, node_class, x=0, y=0, *args):
        return MockNode()


class MockNode(MockUnrealObject):
    def find_pin(self, pin_name):
        return MockPin()

    def get_pin_at_index(self, index):
        return MockPin()


class MockPin(MockUnrealObject):
    def make_link_to(self, other_pin):
        pass


class MockMaterial(MockUnrealObject):
    """Mock Material class."""

    def create_material_expression(self, expression_class):
        return MockMaterialExpression()


class MockMaterialExpression(MockUnrealObject):
    def connect_expression(self, from_expr, to_input, from_output):
        pass


class MockMaterialInstanceConstant(MockUnrealObject):
    """Mock MaterialInstanceConstant class."""
    pass


class MockVector2D:
    """Mock Vector2D class."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class MockVector:
    """Mock Vector class."""
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


class MockRotator:
    """Mock Rotator class."""
    def __init__(self, pitch=0, yaw=0, roll=0):
        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll


class MockAnchors:
    """Mock Anchors class."""
    def __init__(self, min_x=0, min_y=0, max_x=1, max_y=1):
        self.minimum = MockVector2D(min_x, min_y)
        self.maximum = MockVector2D(max_x, max_y)


class MockSlateBrush:
    """Mock SlateBrush class."""
    def __init__(self, image_path=None):
        self.image_path = image_path


class MockAssetTools:
    """Mock AssetTools class."""

    def create_asset(self, name, path, asset_class, factory=None):
        instance = asset_class()
        instance._properties['name'] = name
        instance._properties['path'] = path
        return instance

    def duplicate_asset(self, new_name, path, original_asset):
        return MockUnrealObject()


class MockAssetToolsHelpers:
    """Mock AssetToolsHelpers class."""

    @staticmethod
    def get_asset_tools():
        return MockAssetTools()


class MockEditorAssetLibrary:
    """Mock EditorAssetLibrary class."""

    @staticmethod
    def load_asset(path):
        return MockUnrealObject()

    @staticmethod
    def does_directory_exist(path):
        return True

    @staticmethod
    def make_directory(path):
        return True

    @staticmethod
    def list_assets(path, recursive=False):
        return []

    @staticmethod
    def delete_asset(path):
        return True

    @staticmethod
    def rename_asset(old_path, new_path):
        return True

    @staticmethod
    def find_package_referencers_for_asset(path):
        return []

    @staticmethod
    def save_asset(path):
        return True


class MockEditorLevelLibrary:
    """Mock EditorLevelLibrary class."""

    @staticmethod
    def get_editor_world():
        return MockWorld()

    @staticmethod
    def get_all_level_actors(level=None):
        return []

    @staticmethod
    def spawn_actor_from_class(actor_class, location, rotation=None):
        return MockActor()

    @staticmethod
    def get_selected_level_actors():
        return []

    @staticmethod
    def destroy_actor(actor):
        return True

    @staticmethod
    def new_level(path):
        return MockWorld()


class MockWorld(MockUnrealObject):
    """Mock World class."""

    def get_current_level(self):
        return MockLevel()


class MockLevel(MockUnrealObject):
    pass


class MockActor(MockUnrealObject):
    """Mock Actor class."""

    def get_actor_location(self):
        return MockVector()

    def set_actor_location(self, location, sweep=False, teleport=False):
        pass


class MockEditorUtilityLibrary:
    """Mock EditorUtilityLibrary class."""

    def get_selected_assets(self):
        return []


class MockEditorUtilitySubsystem(MockUnrealObject):
    """Mock EditorUtilitySubsystem class."""

    def create_widget(self, widget_class, z_order=0):
        return MockWidget()


class MockGameplayStatics:
    """Mock GameplayStatics class."""

    @staticmethod
    def play_sound_at_location(world, sound, location, volume_multiplier=1.0, pitch_multiplier=1.0):
        return MockUnrealObject()

    @staticmethod
    def play_sound_2d(world, sound, volume_multiplier=1.0, pitch_multiplier=1.0):
        return MockUnrealObject()


# Factory classes
class MockAnimationSequenceFactory(MockUnrealObject):
    pass


class MockAnimationMontageFactory(MockUnrealObject):
    pass


class MockBlendSpaceFactory1D(MockUnrealObject):
    pass


class MockAnimationStateMachineFactory(MockUnrealObject):
    pass


class MockSoundWaveFactory(MockUnrealObject):
    pass


class MockSoundCueFactory(MockUnrealObject):
    pass


class MockSoundMixFactory(MockUnrealObject):
    pass


class MockSoundClassFactory(MockUnrealObject):
    pass


class MockSoundAttenuationFactory(MockUnrealObject):
    pass


class MockWidgetBlueprintFactory(MockUnrealObject):
    pass


class MockBlueprintFactory(MockUnrealObject):
    pass


class MockSoundEffectSourcePreset(MockUnrealObject):
    pass


# Node classes
class MockK2Node_VariableGet(MockUnrealObject):
    pass


class MockK2Node_VariableSet(MockUnrealObject):
    pass


class MockK2Node_If(MockUnrealObject):
    pass


class MockK2Node_ForLoop(MockUnrealObject):
    pass


class MockK2Node_CallFunction(MockUnrealObject):
    pass


# UI classes
class MockButton(MockUnrealObject):
    pass


class MockTextBlock(MockUnrealObject):
    pass


class MockImage(MockUnrealObject):
    pass


class MockUserWidget(MockUnrealObject):
    pass


def get_editor_subsystem(subsystem_class):
    """Mock get_editor_subsystem function."""
    if subsystem_class == MockEditorUtilitySubsystem:
        return MockEditorUtilitySubsystem()
    return MockUnrealObject()


# Module-level attributes to mimic unreal module
AnimationSequence = MockAnimationSequence
AnimNotify = MockAnimNotify
AnimationMontage = MockAnimationMontage
BlendSpace1D = MockBlendSpace1D
AnimationStateMachine = MockAnimationStateMachine
SoundWave = MockSoundWave
SoundCue = MockSoundCue
SoundMix = MockSoundMix
SoundClass = MockSoundClass
SoundAttenuation = MockSoundAttenuation
WidgetBlueprint = MockWidgetBlueprint
Blueprint = MockBlueprint
Material = MockMaterial
MaterialInstanceConstant = MockMaterialInstanceConstant

Vector2D = MockVector2D
Vector = MockVector
Rotator = MockRotator
Anchors = MockAnchors
SlateBrush = MockSlateBrush

AssetToolsHelpers = MockAssetToolsHelpers
EditorAssetLibrary = MockEditorAssetLibrary
EditorLevelLibrary = MockEditorLevelLibrary
EditorUtilityLibrary = MockEditorUtilityLibrary
EditorUtilitySubsystem = MockEditorUtilitySubsystem
GameplayStatics = MockGameplayStatics

AnimationSequenceFactory = MockAnimationSequenceFactory
AnimationMontageFactory = MockAnimationMontageFactory
BlendSpaceFactory1D = MockBlendSpaceFactory1D
AnimationStateMachineFactory = MockAnimationStateMachineFactory
SoundWaveFactory = MockSoundWaveFactory
SoundCueFactory = MockSoundCueFactory
SoundMixFactory = MockSoundMixFactory
SoundClassFactory = MockSoundClassFactory
SoundAttenuationFactory = MockSoundAttenuationFactory
WidgetBlueprintFactory = MockWidgetBlueprintFactory
BlueprintFactory = MockBlueprintFactory
SoundEffectSourcePreset = MockSoundEffectSourcePreset

K2Node_VariableGet = MockK2Node_VariableGet
K2Node_VariableSet = MockK2Node_VariableSet
K2Node_If = MockK2Node_If
K2Node_ForLoop = MockK2Node_ForLoop
K2Node_CallFunction = MockK2Node_CallFunction

Button = MockButton
TextBlock = MockTextBlock
Image = MockImage
UserWidget = MockUserWidget
